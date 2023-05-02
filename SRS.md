# Software Requirements Specification for BeeSocial

Version 1.0 approved

Prepared by Heather Smith, Melanie Lent, Nicholas Warner
02/18/2021

## Revision History

- Name, Date, Reason For Changes, Version
- All , 02/18/2021 , Init , 0.1

## 1. Introduction

### 1.1 Purpose

BeeSocial 0.1 is being created to enhance the reach of scientists and the general public. Particularly, scientists to increase their reach when trying to identify the spread of invasive species or other niche tasks which rely on input from the general public.

### 1.2 Document Conventions

Document conventions will be consistent with the implementation of Ninja in HTML and Flask as our backend.  tbc

### 1.3 Intended Audience and Reading Suggestions

Our intended audience is the general public but moreso intended for scientists. All things science. 

### 1.4 Product Scope

The murder hornets are a potential catastrophe which required US regulators to quickly adapt their resources to handling this problem as there is already a problem with the North American HoneyBee population.  In response, an app was created so people of the public could submit potential sighting of the hornet along with other relevant data such as latitude and longitude.  Each submission is required to be looked at and accessed by hand which takes more time than the US can afford as the number of reported sightings exceeds 50,000 and the growth of the Murder Hornet population is exponential. 

This application has a goal to close the gap in the effectiveness in reporting.  Posts can be submitted and the easily false sightings can be weeded out as other member of the community on this platform will give feedback and vote on the relevance of sightings. 


### 1.5 References

Our style guide is to keep things clean, consistent, and easy to use. All features and settings should be easy for a user to find, and self-explanatory. There should be few, if any, features that require additional reading to understand.

## 2. Overall Description

### 2.1 Product Perspective

If one counts the frameworks used to run the website, then the project is not wholly self-contained, but it is otherwise its own product. It is not supplemental to any existing product, and no third-party software is needed to use or access it.

Images on the website are intended to be hosted externally. 

### 2.2 Product Functions

Image uploading

Like/Dislike | Upvote/Downvote 

Reposting? 

Permissions/User Roles

As we need to make distictions of who the scientists are in the community and who are pubic participants, user roles and permissions are required. Becoming a scientist on the platform would require an additional means of registration.  Furthermore, implementing a system which can rate public users on their reliability on trustworthyness would be of high interest to Bee Social.   

### 2.3 User Classes and Characteristics

Primarily, the developers expect educated individuals, or those seeking information on specific scientific topics, to use this platform. 

### 2.4 Operating Environment

Operating Requirements are only constrained to and up-to-date web browser.

### 2.5 Design and Implementation Constraints

<Describe any items or issues that will limit the options available to the
developers. These might include: corporate or regulatory policies; hardware
limitations (timing requirements, memory requirements); interfaces to other
applications; specific technologies, tools, and databases to be used; parallel
operations; language requirements; communications protocols; security
considerations; design conventions or programming standards (for example, if the
customer’s organization will be responsible for maintaining the delivered
software).>

### 2.6 User Documentation

Documentation should be created along with the development of the project.  

### 2.7 Assumptions and Dependencies

<List any assumed factors (as opposed to known facts) that could affect the
requirements stated in the SRS. These could include third-party or commercial
components that you plan to use, issues around the development or operating
environment, or constraints. The project could be affected if these assumptions
are incorrect, are not shared, or change. Also identify any dependencies the
project has on external factors, such as software components that you intend to
reuse from another project, unless they are already documented elsewhere (for
example, in the vision and scope document or the project plan).>

## 3. External Interface Requirements

### 3.1 User Interfaces

Bootstrap will be used to create a simple user interface.  The interface should be intuitive and easy to use, especially how familiar the site will feel to other social media platforms.

### 3.2 Hardware interfaces

Take photos from inside the app would require a camera.

Any kind of information related to location should be required from some kind of GPS hardware.  Manual input of location is open to exploitation and should only be considered in rare circumstances. 

### 3.3 Software Interfaces

<Describe the connections between this product and other specific software
components (name and version), including databases, operating systems, tools,
libraries, and integrated commercial components. Identify the data items or
messages coming into the system and going out and describe the purpose of each.
Describe the services needed and the nature of communications. Refer to
documents that describe detailed application programming interface protocols.
Identify data that will be shared across software components. If the data
sharing mechanism must be implemented in a specific way (for example, use of a
global data area in a multitasking operating system), specify this as an
implementation constraint.>

### 3.4 Communications Interfaces

<Describe the requirements associated with any communications functions required
by this product, including e-mail, web browser, network server communications
protocols, electronic forms, and so on. Define any pertinent message formatting.
Identify any communication standards that will be used, such as FTP or HTTP.
Specify any communication security or encryption issues, data transfer rates,
and synchronization mechanisms.>

## 4. System Features

<This template illustrates organizing the functional requirements for the
product by system features, the major services provided by the product. You may
prefer to organize this section by use case, mode of operation, user class,
object class, functional hierarchy, or combinations of these, whatever makes the
most logical sense for your product.>

<You may modify the structure of this secture according to the software process
you are using for this project. For example, if you are using agile (or some of
its derivations) and you need to format the features in terms of user stories,
you may replace the format below with your own adaptation for each user story.>

### 4.1 System Feature 1

Create Scientific Study Groups.  These groups can act like a network to assist scientists who would benefit from the influence of the public.  Such that, when murder hornets are being tracked, the public can upload photos and experiences relevant to the study.  The purpose of creating a solid network where multiple person give input is a system where the community upvotes and downvotes to create a scale of importance.  For example, users upload thousands of images which are considered to be possible sightings of this insect.  Of the tens of thousands, very few are actual sightings or should be considered for investigation.  If there was a reliable community to upvote and downvote the uploads, the work of the scientist would be cut out, straightforward, and clear.  This may increase the effectiveness of their work at an unknown but assured rate. 

### 4.1.1 Description and Priority

Image Uploading as it is the best way to identify said Hornets. 

<Provide a short description of the feature and indicate whether it is of High,
Medium, or Low priority. You could also include specific priority component
ratings, such as benefit, penalty, cost, and risk (each rated on a relative
scale from a low of 1 to a high of 9).>

### 4.1.2 Stimulus/Response Sequences

<List the sequences of user actions and system responses that stimulate the
behavior defined for this feature. These will correspond to the dialog elements
associated with use cases.>

### 4.1.3 Functional Requirements

<Itemize the detailed functional requirements associated with this feature.
These are the software capabilities that must be present in order for the user
to carry out the services provided by the feature, or to execute the use case.
Include how the product should respond to anticipated error conditions or
invalid inputs. Requirements should be concise, complete, unambiguous,
verifiable, and necessary. Use "TBD" as a placeholder to indicate when necessary
information is not yet available.>

<Each requirement should be uniquely identified with a sequence number or a
meaningful tag of some kind.>

- REQ-1:
- REQ-2:

### 4.2 System Feature 2 (and so on)

## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements

Must be able to facilitate image handling.  

Must be able to scale records of upvotes and downvotes in a dynamic way.  

### 5.2 Safety requirements

Terms & Conditions 

No matter the study it will be up to the user to participate with discretion and use this discretion in any related activities. 

### 5.3 Security Requirements

As we expect this application to interface communication with the public, security requirements would be relatively minimal as the information being discussed or communicated would not need to be protected in any way.  

### 5.4 Software Quality Attributes

<Specify any additional quality characteristics for the product that will be
important to either the customers or the developers. Some to consider are:
adaptability, availability, correctness, flexibility, interoperability,
maintainability, portability, reliability, reusability, robustness, testability,
and usability. Write these to be specific, quantitative, and verifiable when
possible. At the least, clarify the relative preferences for various attributes,
such as ease of use over ease of learning.>

### 5.5 Business Rules

<List any operating principles about the product, such as which individuals or
roles can perform which functions under specific circumstances. These are not
functional requirements in themselves, but they may imply certain functional
requirements to enforce the rules.>

## 6. Other Requirements

<Define any other requirements not covered elsewhere in the SRS. This might
include database requirements, internationalization requirements, legal
requirements, reuse objectives for the project, and so on. Add any new sections
that are pertinent to the project.>

## Appendix A: Glossary

<Define all the terms necessary to properly interpret the SRS, including
acronyms and abbreviations. You may wish to build a separate glossary that spans
multiple projects or the entire organization, and just include terms specific to
a single project in each SRS.>

## Appendix B: Analysis Models

<Optionally, include any pertinent analysis models, such as data flow diagrams,
class diagrams, state-transition diagrams, or entity-relationship diagrams.>

## Appendix C: To Be Determined List

<Collect a numbered list of the TBD (to be determined) references that remain in
the SRS so they can be tracked to closure.>
