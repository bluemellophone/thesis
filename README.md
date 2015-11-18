2015 Master's Thesis Source Files
=================================

Introduction
------------

This repository holds the source files used to generate my 2015 Master's Thesis
entitled, &rdquo;Photographic Censusing of Zebra and Giraffe in the Nairobi
National Park&rdquo;.

This thesis document is meant to be a partial fullfillment of the requirements
for a M.S. degree in Computer Science at RPI.  The thesis is paired with an oral
presentation (given in August 2015) and an accompanying poster.  The final draft
was submitted to the University in November 2015 for graduation December, 2015.

Master's Committee
* Charles Stewart, Thesis Advisor, Computer Science Department Chair
* Barbara Cutler
* B&uuml;lent Yener

*Note: From feedback from the committee after the oral presentation, the title
of the thesis was changed from &rdquo;How Many Plains Zebras And Masai Giraffes
are in the Nairobi National Park? - A Case Study in Computer Vision and Citizen
Science&rdquo; to &rdquo;Photographic Censusing of Zebra and Giraffe in the
Nairobi National Park&rdquo;*


Abstract
--------
Establishing a population estimate for the plains zebras and Masai giraffes in
the Nairobi National Park (NNP) can be a challenging task due to the large size
of the conservation area and large population.  Making the situation worse, the
NNP is not fenced on its southern boundary, which makes traditional counting
methods impractical and unpredictable due to the park's arbitrary population.
Traditional and invasive identification methods (e.g. ear tags, ear notches,
radio collars) are costly and infeasible for large populations.  As an
alternative, we propose a passive, appearance-based approach that uses images of
animals taken by volunteer &ldquo;citizen scientists&rdquo; to identify
individuals.  Image data is analyzed using our prototype IBEIS computer vision
algorithm, which recognizes animals based solely on their appearance.  The
collection of images over time allows for a more comprehensive ecological
analysis of the animal population and the park's ecosystem.   By providing
actionable ecological data, our method allows the conservationists in the NNP to
make data-driven decisions in order to accomplish their conservation goals.

In March of 2015, the IBEIS team helped to administer *The Great Zebra & Giraffe
Count* (GZGC), which collected 9,406 images from 58 volunteer citizen
scientists.  The contributed images yielded a total of 8,659 sightings of plains
zebras (Equus quagga), of which we identified 1,258 individuals.  We performed a
photographic censusing, or photographic mark-recapture (PMR) study, on the last
two days of data collection and, using the Lincoln-Peterson method, estimated a
total of 2,307 &plusmn; 366 zebras in the NNP (confidence of 95%).  The IBEIS
team also analyzed images of Masai giraffes (Giraffa camelopardalis
tippelskirchi), which yielded a total of 1,258 sightings.  Of the sighted
giraffes, we found 103 individuals and calculated a Peterson-Lincoln Index of
119 &plusmn; 48.

To our knowledge, this is the first time a population estimate of the plains
zebras and Masai giraffes has ever been performed using an automated appearance-
based approach.  We also believe that the GZGC was the largest citizen science
data collection event ever performed inside the park, to date.


Software Repositories
---------------------
* https://github.com/Erotemic/ibeis
* https://github.com/bluemellophone/gzc-client
* https://github.com/bluemellophone/gzc-server


Build Instructions
------------------
* Install LaTeX and BibTeX
* Build rpithesis.tex
* View PDF document in rpithesis.pdf


Degree Coursework [credits]
---------------------------
* Computer Operating Systems [3]
* Cryptography &ambs; Network Security I [3]
* Randomized Algorithms [3]
* Cryptography &ambs; Network Security II [3]
* Machine Learning [3]
* Programming Languages [3]
* Computational Vision [3]
* Neural Networks for Computer Vision [3]
* Master's Thesis Credits (Dr. Stewart) [6]


Fields
------
* Computer Science
* Ecology


Keywords
--------
* photographic censusing
* Kenya
* IBEIS
* Great Zebra & Giraffe Count
* citizen science
* computer vision


Zotero References
-----------------
https://www.zotero.org/groups/chucks_rpi_vision_group/items/collectionKey/7K23MMC8


Acknowledgements
----------------
*The Great Zebra &ambs; Giraffe Count* (GZGC) was powered and administered by
the IBEIS team with notable help from Dr. Paula Kahumbu and staff at Wildlife
Direct in Nairobi, Kenya.  The IBEIS team would like to thank the people and
government of Kenya for supporting this research (Permit
&#35; NACOSTI/P/14/1003/1628), with special recognition to Senior Warden of the
Nairobi National Park, Nely Palmeris, and Macharia &ldquo;Michael&rdquo;
Kimura of the Kenyan Wildlife Service (KWS).  Other contributions to this thesis
were provided by Clara Machogu, Marco Maggioni, Jon Crall, Hendrik Weideman,
Michael Brown, and Zachary Jablons.  I would like to thank Dr. Tanya
Berger-Wolf, Dr. Daniel Rubenstein, and my master committee members, Dr. Barbara
Cutler and Dr. B&uuml;lent Yener, for their valuable feedback.  I would also
like to give a special thank you to my Ph.D. advisor, Dr. Charles Stewart, who
has patiently guided me to this milestone of my academic career.

The open-source software and research detailed in this thesis was supported by
Rensselaer Polytechnic Institute (RPI) and with financial support from NSF EAGER
Grant (Award &#35; 1453503) *Collaborative Research: EAGER: Prototype of an
Image-Based Ecological Information System (IBEIS)*.

Lastly, but most importantly, I would like to thank my wife, Lindsay, for
providing patient, never-failing support.  Her dedication to my academic career
and intellectual progress has been the best example of sacrificial love I have
ever had the privilege to personally experience.

resources/logo_ibeis.png
resources/logo_wd_alpha.png