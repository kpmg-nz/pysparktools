#!/usr/bin/env python

from setuptools import setup
import jinja2
import os
from dunamai import (
    bump_version,
    serialize_pep440,
    serialize_pvp,
    serialize_semver,
    Version,
)

# get version of package from the GIT version
version = Version.from_git()
format_jinja = """
    {%- if distance == 0 -%}
        {{ serialize_pep440(base, stage, revision) }}
    {%- else -%}
        {{ serialize_pep440(base, stage, revision, post=commit|int(base=16)) }}
    {%- endif -%}
"""
default_context = {
    "base": version.base,
    "version": version,
    "stage": version.stage,
    "revision": version.revision,
    "distance": version.distance,
    "commit": version.commit,
    "dirty": version.dirty,
    "env": os.environ,
    "bump_version": bump_version,
    "tagged_metadata": version.tagged_metadata,
    "serialize_pep440": serialize_pep440,
    "serialize_pvp": serialize_pvp,
    "serialize_semver": serialize_semver,
}
serialized_version = jinja2.Template(format_jinja).render(
    **default_context
)

setup(
    name='pysparktools',
    version=serialized_version,
    description='Python pckage to simplify working with pyspark by using familiar pandas syntax.',
    python_requires='>=3.9.0, <3.10',
    install_requires=[
    ]
)