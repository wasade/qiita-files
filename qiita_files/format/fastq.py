# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The Qiita Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------


def _phred_to_ascii(a, offset):
    """Convert Phred quality score to ASCII character with specified offset"""
    return (a + offset).tobytes()


def _phred_to_ascii33(a):
    """Convert Phred quality score to ASCII character with offset of 33"""
    return _phred_to_ascii(a, 33)


def _phred_to_ascii64(a):
    """Convert Phred quality score to ASCII character with offset of 64"""
    return _phred_to_ascii(a, 64)


def format_fastq_record(seqid, seq, qual, phred_offset=33):
    """Format a FASTQ record

    Parameters
    ----------
    seqid : bytes
        The sequence ID
    seq : bytes
        The sequence
    qual : np.array of int8
        The quality scores
    phred_offset : int, either 33 or 64
        Set a phred offset

    Returns
    -------
    bytes : a string representation of a single FASTQ record
    """
    if phred_offset == 33:
        phred_f = _phred_to_ascii33
    elif phred_offset == 64:
        phred_f = _phred_to_ascii64
    else:
        raise ValueError("Unknown phred offset: %d" % phred_offset)

    return b'\n'.join([b"@" + seqid, seq, b'+', phred_f(qual), b''])
