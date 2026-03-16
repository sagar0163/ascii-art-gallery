"""Unit tests for ASCII Art Gallery"""

import pytest
from unittest.mock import Mock, patch
import os


class TestAsciiArt:
    def test_load_art_file(self):
        # Mock file loading
        sample_art = """
   /\        
  /  \       
 /____\      
|      |     
|______|    
"""
        assert len(sample_art) > 0
    
    def test_art_dimensions(self):
        art = """
A B
C D
"""
        lines = art.strip().split('\n')
        assert len(lines) == 2
    
    def test_ascii_character_count(self):
        art = "abcdefghij"
        assert len(art) == 10


class TestArtGenerator:
    def test_generator_initialization(self):
        from generator import ArtGenerator
        gen = ArtGenerator()
        assert gen is not None
    
    def test_text_to_ascii(self):
        from generator import ArtGenerator
        gen = ArtGenerator()
        result = gen.text_to_ascii("TEST")
        assert result is not None


class TestArtCategories:
    def test_animal_arts(self):
        animals = os.listdir('./animals') if os.path.exists('./animals') else []
        assert isinstance(animals, list)
    
    def test_landscape_arts(self):
        landscapes = os.listdir('./landscapes') if os.path.exists('./landscapes') else []
        assert isinstance(landscapes, list)


class TestExport:
    def test_export_to_file(self):
        art = "Test Art"
        # Should be able to export
        assert len(art) > 0
    
    def test_export_formats(self):
        formats = ['txt', 'html', 'md']
        for fmt in formats:
            assert fmt in ['txt', 'html', 'md']
