#!/usr/bin/env python3
"""
Formula taken from:

Multiconfigurational Quantum Chemistry
Björn Roos (told by VV)

Department of Theoretical Chemistry
Lund University

http://www.molcas.org/VV/Fribourg2.pdf
"""

import sys
import argparse as ap
from scipy.special import comb as binom
from num2words import num2words


def get_args(arguments):
    """ parse the input """

    parser = ap.ArgumentParser(
        description=(
            "Calculates the number of configuration state functions"
            " for CAS calculations."
        )
    )
    parser.add_argument("number_of_electrons", type=int)
    parser.add_argument("number_of_molecular_orbitals", type=int)
    parser.add_argument(
        "spin_quantum_number", nargs="?", default=0.0, type=float
    )
    parser.add_argument("--language", "-lang", nargs="?", default="de")

    return parser.parse_args(arguments)


def number_of_configuration_state_functions(n_mo, n_el, spin):
    """ Number of CSFs """
    factor_1 = (2 * spin + 1) / (n_mo + 1)
    factor_2 = binom(n_mo + 1, 1 / 2 * n_el - spin)
    factor_3 = binom(n_mo + 1, 1 / 2 * n_el + spin + 1)
    return int(factor_1 * factor_2 * factor_3)


if __name__ == "__main__":
    ARGS = get_args(sys.argv[1:])
    N_CSF = number_of_configuration_state_functions(
        ARGS.number_of_molecular_orbitals,
        ARGS.number_of_electrons,
        ARGS.spin_quantum_number,
    )
    print(f"N(CSF): {N_CSF:_}")
    print(f"        {num2words(N_CSF, lang=ARGS.language)}")
