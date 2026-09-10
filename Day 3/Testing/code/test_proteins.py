import pytest

import proteins

from proteins import number_negatives

def number_negatives(seq):
    """Number of negative residues a protein sequence"""
    # Convert sequence to upper case
    seq = seq.upper()

    # Count E's and D's, since these are the negative residues
    return seq.count('E') + seq.count('D')


def test_number_negatives_for_single_AA():
    """Perform unit tests on number_negative for single AA"""
    assert number_negatives('E') == 1
    assert number_negatives('D') == 1


def test_number_negatives_for_empty():
    """Perform unit tests on number_negative for empty entry"""
    assert number_negatives('') == 0


def test_number_negatives_for_short_sequence():
    """Perform unit tests on number_negative for short sequence"""
    assert number_negatives('ACKLWTTAE') == 1
    assert number_negatives('DDDDEEEE') == 8


def test_number_negatives_for_lowercase():
    """Perform unit tests on number_negative for lowercase"""
    assert number_negatives('acklwttae') == 1


def test_number_negatives_for_invalid_amino_acid():
    with pytest.raises(RuntimeError) as excinfo:
        proteins.number_negatives('K')
    excinfo.match("Z is not a valid amino acid")
