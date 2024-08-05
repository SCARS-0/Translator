import pytest
from googletrans import Translator, LANGUAGES
from project import TranslateClass  # Ensure you replace this with the actual name of your script

def test_translation_to_hindi():
    word = "Hello"
    lang = "hi"
    translation = TranslateClass(word, lang)
    assert "Language:" in str(translation)
    assert "English" in str(translation)
    assert "Hello" in str(translation)
    assert "Hindi" in str(translation)  # Check if the table has 'Hindi'

def test_translation_to_kannada():
    word = "Hello"
    lang = "kn"
    translation = TranslateClass(word, lang)
    assert "Language:" in str(translation)
    assert "English" in str(translation)
    assert "Hello" in str(translation)
    assert "Kannada" in str(translation)  # Check if the table has 'Kannada'

def test_translation_error():
    word = "Hello"
    lang = "unknown_language_code"  # Invalid language code
    translation = TranslateClass(word, lang)
    assert "Translation Error" in str(translation)

if __name__ == "__main__":
    pytest.main()
