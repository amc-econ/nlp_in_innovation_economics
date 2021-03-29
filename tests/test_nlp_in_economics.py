#!/usr/bin/env python

"""Tests for `nlp_in_economics` package."""


import unittest
from click.testing import CliRunner

from nlp_in_economics import nlp_in_economics
from nlp_in_economics import cli


class TestNlp_in_economics(unittest.TestCase):
    """Tests for `nlp_in_economics` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'nlp_in_economics.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
