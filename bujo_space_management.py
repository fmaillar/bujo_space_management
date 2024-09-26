#!/usr/bin/python3
"""This script compute the distribution of section of a page of a bullet journal.

The first argument is the width of the page in term of bullet spacing and
the second is the height.
"""

import argparse


class Page:
    """This class reprensent a sheet with width and height."""

    def __init__(self, width, height):
        """Initiate the class."""
        self.width = width
        self.height = height

    def distribute_bullets(self, total_bullets, sections):
        """
        Distributes bullets into equal sections with gaps if necessary.

        :param total_bullets: Total number of bullets (width or height)
        :param sections: Number of sections to divide the space into
        :return: List of integers representing the size of each section
        """
        # Base size of each section
        base_size = total_bullets // sections
        # Number of remaining bullets (gaps)
        remainder = total_bullets % sections

        # Create a list where each section has the base size
        section_sizes = [base_size] * sections

        # Distribute the remainder (gaps) across the first sections
        for i in range(remainder):
            section_sizes[i] += 1

        return section_sizes

    def print_distributions(self):
        """
        Print the list of the distribution.

        :param total_bullets: Total number of bullets (width or height)
        :param sec_list: List of integers representing the size of each section
        (output of distribute_bullets method)
        """
        for total_bullets in (self.width, self.height):
            print(f"""{40*"-"}""")
            for idx in range(2, 11):
                distribution = self.distribute_bullets(total_bullets, idx)
                print(
                        f"""distribution ({total_bullets} bullets, {idx:2} sections): {distribution}"""
                )


parser = argparse.ArgumentParser(
    description="""Process the distribution from the width and the height."""
)
parser.add_argument(
    "width",
    metavar="width",
    type=int,
    help="""the width in
                    bullet of the page.""",
)
parser.add_argument(
    "height",
    metavar="height",
    type=int,
    help="""the height
                    in bullet of the page.""",
)
args = parser.parse_args()

page = Page(args.width, args.height)
page.print_distributions()
