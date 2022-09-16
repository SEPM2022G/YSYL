# YSYL

You Stack You Lose, The project for Group G 2022

## Contributing

All changes to the main branch are made through pull requests on GitHub. In
order to contribute, create a branch with your changes and submit a pull request
to `main`. Include a title and description of your changes to help reviewers
understand your changes. 

```
Feature: Save a state in the statemanager

Added a function to save a new state in the statemanager component. 
```

**Important** Never commit and push directly to the main branch!

When naming branches start off with a "tag" describing what kind of changes the
branch includes (feature, fix, hotfix, etc..) and follow with a
description of what you are working on. It is also a good idea to mention what
part of the system the changes are related to if it helps identifying the purpose
of the branch. The branch naming convention exists to make it easier figuring
out what a branch contains and to force the author to keep his/her changes
coherent with the naming. Try to avoid being overly specific to keep the names
to a reasonable length, common sense is more important than any convention!

```
feat-validator
feat-savestate
feat-io-processfile
fix-validator
hotfix-imports
feat-alphabetapruning

```

All changes should be reviewed by a minimum of `1` other person after submitting
a pull request to ensure that other members can weigh in on the changes. Try to
avoid having people that are involved with the changes review their own pull
request, even if this is tempting.

When merging pull requests we `Squash and merge` to the main branch. Squashing
combines all the commits in the pull request and allows us to use our own format
for individual commits on individual branches and still keep the history of the
main branch in a coherent format.

## Reviewing
When reviewing a pull request, make sure that it meets the most important
guidelines before merging:

- Is the feature/fix well defined and only solve a single or narrow group of
problems?

- Are tests written?

- No magic constants, misleading variable names etc..

- Are the changes in the correct component?

Here are some more detailed checks: 
[PR checklist](https://devchecklists.com/pull-requests-checklist/)
