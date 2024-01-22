DJ-LMP1
=======

This is the pre-MVP repository for experimentation.  It is designed to serve as a scratch pad for ideas.
There will be no releases and no organized branching / tag strategy.  It is a place to
incubate and test dj-lmp ideas.

Setup
-----

    git clone https://github.com/csev/dj-lmp1
    cd dj-lmp1
    virtualenv .venv
    source .venv/bin/activate
    pip install django
    python -m django --version
    # Should be 5.0.1
    cp config/settings-sqlite.py config/settings.py

When you come back in, 

    cd dj-lmp1
    source .venv/bin/activate

1EdTech Specifications
======================

https://www.1edtech.org/standards/lti

https://www.imsglobal.org/activity/common-cartridge

https://www.imsglobal.org/activity/onerosterlis

Hierarchy Design Notes
======================

As our first data model exercise, we need to think through a hierarchy as
shown in 1EdTech OneRoster.  At minimum, dj-lmp would want to consume
OneRoster - probably we should plan on producing it as well.  Once you have the
data model, why not?

https://www.imsglobal.org/activity/onerosterlis

This overlaps with LTI in a lot of areas - in particular in Roles:

https://www.imsglobal.org/spec/lti/v1p3/#standardvocabs

The LMS that is best at Hierachy is D2L.  D2L was influential in the creation
of OneRoster.

https://community.d2l.com/brightspace/kb/articles/5399-about-org-unit-type-editor

https://community.d2l.com/brightspace/kb/articles/4529-organizational-units-data-sets

https://docs.valence.desire2learn.com/res/orgunit.html

We need to build a hierarchical data model:

https://stackoverflow.com/questions/192220/what-is-the-most-efficient-elegant-way-to-parse-a-flat-table-into-a-tree/192462#192462

https://www.slideshare.net/billkarwin/models-for-hierarchical-data

https://stackoverflow.com/questions/8252323/mysql-closure-table-hierarchical-database-how-to-pull-information-out-in-the-c

Dr. Chuck built an efficient hierarchy in the tDiscuss code - https://github.com/tsugitools/tdiscus.git

Project Related Installs
------------------------

See the [Getting Started](PROJECT.md) documentation

