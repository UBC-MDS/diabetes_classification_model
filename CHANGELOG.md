# Changelog
2023 December
author: Angela Chen, Ella Hein, Scout McKee, and Sharon Voon.

In this latest December release - Milestone 4, we introduce 
several enhancements, bug fixes, and documentation updates to 
improve the overall functionality and clarity of our project. 
Notably, we've implemented a command in the README to ensure 
full reproducibility of the analysis, accompanied by clear 
setup instructions and guidelines for managing dependencies 
and unnecessary files. We've also addressed inconsistencies 
in testing approaches, specifically removing the if __name__ 
== "main": pytest.main() block to maintain uniformity across 
all tests. Additionally, a bug affecting the display of 
Figure 3 has been resolved, now accurately presenting the 
expected coefficient values. To enhance attribution, author 
names have been included on the rendered report, and DOI's have been
added for all of the references in the bibligraphy. Furthermore, 
the README has undergone refinements, encompassing set-up 
instructions cleanup and the organization of extraneous 
files. We've responded to user queries by providing a 
succinct explanation of how the general health index, a 
critical aspect of our model, is calculated. The analysis 
notebook (.ipynb or .Qmd or *Rmd) is now located in a 
sub-directory called "notebooks" for improved project 
organization, addressing concerns about file clutter in the 
project root. To further streamline the repository, all unnecessary
files have been removed and the .gitignore was updated to prevent
any system-generated files from being pushed. We have also updated 
LICENSE file to include CC BY-NC-ND 4.0 license for our report.

## Features
Reproducibility Command: Added a command in/after the 
analysis section of the README to ensure full 
reproducibility. This includes clear setup instructions, a 
comprehensive list of dependencies, and guidelines for 
archiving unnecessary files such as .DS_Store or .Rhistory.
## Bug Fixes
Testing Consistency: Addressed the inconsistency in testing 
approaches. Removed the if __name__ == "main": pytest.main() 
block to ensure a consistent testing structure across all 
test modules.
Figure Display Issue: Resolved an issue where Figure 3 was 
incorrectly displaying the same image as Figure 2. The 
correct coefficient values are now displayed as intended.

**Evidence of change:** commit 06cf7341ffd61ea7eff31be464893bba965eec1c
with the message "fixed the error in the improper table in report"

## Documentation
Author Attribution: Updated the README file to include 
author names on the rendered report for improved 
attribution.
General Health Index Explanation: Added a brief summary in 
the documentation explaining how the general health index 
is calculated, acknowledging its importance to the model.
**Evidence of change**: 

Summary in README: Enhanced the README with a high-level 
interpretation of analysis findings, providing 1-2 sentences 
on their potential implications. 

References: DOI's were updated for all references, where applicable.

**Evidence of change:** commit 06cf7341ffd61ea7eff31be464893bba965eec1c
with the message "fixed the error in the improper table in report"

## License
CC BY-NC-ND 4.0 License has been included in our LICENSE file 
on the root repository.

**Evidence of change:** see commit 96512eba24c9de48ef3c4c01d386303bb0c83c3e 
where pull request #104 where branch build_report was merged to main

## Other
README Refinement: Ongoing refinement of the README file, 
including set-up instructions cleanup and the organization 
of unnecessary files (e.g., .DS_Store, .Rhistory).

.gitignore Update: All .DS_Store and .Rhistory files have been 
deleted and updated in the gitignore.

**Evidence of change:** see commit 9f40aee3e9002bd2be220e224b5b3de1717fe469
where pull request #96 where branch update-gitignore was merged to main.

Grading Comment Addressed: The analysis notebook is now 
located in a sub-directory called "archieve" for improved 
project organization, addressing concerns about file clutter 
in the project root.

As we release this latest version of our project, we extend 
our heartfelt gratitude to all contributors who have played 
a pivotal role in shaping and refining its functionality. 
Your valuable feedback, suggestions, and diligent efforts 
have significantly contributed to the project's improvement. 
Your commitment to excellence has not only strengthened our 
codebase but also fostered a collaborative and supportive 
community. We deeply appreciate your dedication and look 
forward to continuing this journey together. Thank you for 
being an integral part of our project's success.
