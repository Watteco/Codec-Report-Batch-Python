Python implementation of `br_uncompress`

# Requirements 

This code needs Python 3.6 or more recent version.

# Usage

## From the command line

The usage is quite similar to the C version.

Here are 2 examples:

      py br_uncompress.py -a 3 2,1.0,12 -if $10$27$00$80$03$93$20$18$00$80$10$81$83$07$0d$45$85$10$05

Or

      py br_uncompress.py -a 3 2,10,9 1,10,7 4,30,10 3,10,4 5,10,6 6,1,4 -if 404780800a5800000442ca8a4048fd395c817e21cb9a40028fd5379de3768b4f816e75a6e376006e2d800066

Here is the usage (obtained by executing `./br_uncompress.py -h`):

    usage: br_uncompress.py [-h] [-a] [-t TIMESTAMP] [-v]
                            tagsz [command [command ...]] [-if]



    positional arguments:
      tagsz
      command               In form of "taglbl,resol,sampletype" "..." or
                            "taglbl,resol,sampletype,taglbl"

    optional arguments:
      -h, --help            show this help message and exit
      -a, --ascii           Input buf must be considered as ascii hexa bytes
                            either than usual raw bytes: 'hhhhhh...' or 'hh hh
                            hh...' or '$HH$HH$HH...'
      -t TIMESTAMP, --timestamp TIMESTAMP
                            Timestamp of the measure in iso format like
                            2018-11-05T10:35:09.685Z
      -v, --verbose         Print details of the process on standard output


## As a module

The uncompress function can be imported in another Python code:

    from br_uncompress import uncompress
    result = uncompress(
        3,
        [{"taglbl": 2, "lblname": "temperature", "resol": 1.0, "sampletype": 12}],
        "$10$27$00$80$03$93$20$18$00$80$10$81$83$07$0d$45$85$10$05",
    )

Without lblname:

    from br_uncompress import uncompress
    result = uncompress(
        1,
        [
            {"taglbl": 0, "resol": 1, "sampletype": 10},
            {"taglbl": 1, "resol": 1, "sampletype": 1},
        ],
        "20100000a020a8010000004401e297ad40871b770e377b",
    )


With a batch absolute timestamp:

    from br_uncompress import uncompress
    result = uncompress(
        1,
        [
            {"taglbl": 0, "resol": 1, "sampletype": 10},
            {"taglbl": 1, "resol": 1, "sampletype": 1},
        ],
        "20100000a020a8010000004401e297ad40871b770e377b",
        "2018-11-05T10:35:09.685Z",
    )

# Testing

Tests are written in `test_br_uncompress.py`. Py.test module is needed to run them.

Install py.test by doing:

    pipenv install --dev

Or directly with pip

    pip install pytest

