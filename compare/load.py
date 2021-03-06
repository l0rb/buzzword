import os
from .utils import store_buzz_raw, _is_meaningful, _handle_page_numbers
from .models import PDF, OCRUpdate, TIF
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

import pyocr

from PIL import Image

from buzz import Collection

def _get_ocr_engine(lang):
    """
    todo: handle english and other spacy languages

    * add to tessdata
    * make a mapping of language names to tess models
    """
    tools = pyocr.get_available_tools()
    tool = tools[0]
    # langs = tool.get_available_languages()
    # lang = langs[0]
    return tool, "deu_frak2"


def load_tif_pdf_plaintext(corpus):
    """
    From TIF files, convert to PDF for display, and get OCR
    via pyocr/tesseract

    todo: configure multilingual support
    todo: save as little as possible here, as OCR is slow!

    """
    collection = Collection(corpus.path)
    ocr_engine, lang_chosen = _get_ocr_engine(corpus.language.name)
    tot = len(collection.tiff.files)
    for i, tif_file in enumerate(collection.tiff.files):
        tif_path = tif_file.path
        pdf_path = tif_path.replace('/tiff/', "/pdf/").replace(".tif", ".pdf")
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
        name = os.path.basename(tif_path)
        name = os.path.splitext(name)[0]
        # make pdf if need be
        if not os.path.isfile(pdf_path):
            image = Image.open(tif_path)
            image.save(pdf_path)

        # todo: use get_or_create
        pdf, pdf_created = PDF.objects.get_or_create(
            name=name, num=i, path=pdf_path, slug=corpus.slug
        )
        tif, tif_created = TIF.objects.get_or_create(
            name=name, num=i, path=tif_path, slug=corpus.slug
        )

        if pdf_created:
            pdf.save()
        if tif_created:
            tif.save()

        if pdf_created or tif_created:
            print(f"({i+1}/{tot}) Stored PDF/TIF in DB: {pdf.path}")
        if not pdf_created and not tif_created:
            print(f"Exists in DB: {pdf.path} /// {tif.path}")

        # if there is already an OCRUpdate for this PDF, not much left to do
        # todo: fallback to preprocessed/txt ?? otherwise every reload causes
        # ocr to happen
        try:
            OCRUpdate.objects.get(pdf=pdf)
            print(f"OCRUpdate already found for {tif.path}")
            continue
        except ObjectDoesNotExist:
            pass

        if collection.txt and len(collection.txt.files) >= tot:
            path = collection.txt.files[i].path
            print(f"Text file exists at {path}; skipping OCR")
            with open(path, "r") as fo:
                plaintext = fo.read()
            ocr = OCRUpdate(
                slug=corpus.slug, commit_msg="OCR result", text=plaintext, pdf=pdf
            )
            ocr.save()
        else:
            print(f"Doing OCR for {tif.path}")

            # there is no OCRUpdate for this code; therefore we build and save it
            plaintext = ocr_engine.image_to_string(
                Image.open(tif_path),
                lang=lang_chosen,
                builder=pyocr.builders.TextBuilder(),
            )
            plaintext = _handle_page_numbers(plaintext)

            if not _is_meaningful(plaintext, corpus.language.short):
                plaintext = '<meta blank="true"/>'

            ocr = OCRUpdate(
                slug=corpus.slug, commit_msg="OCR result", text=plaintext, pdf=pdf
            )
            print(f"Storing OCR result for {tif_path} in DB...")
            ocr.save()
            # store the result as buzz plaintext corpus for parsing
            store_buzz_raw(plaintext, corpus.slug, pdf_path)
