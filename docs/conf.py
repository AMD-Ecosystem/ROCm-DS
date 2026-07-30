"""Configuration file for the Sphinx documentation builder."""
import os
import shutil
import re

shutil.copy2("../RELEASE.md", "./about/release-notes.md")

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "rocm.docs.amd.com")
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
project = "AMD Data Science"

version = "25.05"
release = version
html_title = "AMD Data Science 25.05 documentation"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2025 Advanced Micro Devices, Inc. All rights reserved."
setting_all_article_info = True
all_article_info_os = ["linux"]
all_article_info_author = ""

#left_nav_title = f"AMD Data Science {version} documentation"

# Required settings
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "rocm-ds",
    # Add any additional theme options here
}
extensions = ["rocm_docs"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

exclude_patterns = ['.venv']
