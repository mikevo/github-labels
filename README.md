# github-labels
This project is meant to purpose a hopefully useful labeling system. Based on the purpose of [Sane GitHub Labels](https://medium.com/@dave_lunny/sane-github-labels-c5d2e6004b63#.8s5wiw1mn) a categorization of the labels is used.

## How to apply them?
The labels can be applied to a github repositories by using [git-labelmaker](https://github.com/himynameisdave/git-labelmaker)

## What are the for?
The currently used Categories are:
* Kind
* Priority
* Status
* Type

The **Kind** of an issue specifies to which part of the project it belongs.

The **Priority** is inspired by the [Eisenhower](http://lifehacker.com/5942972/eisenhower-helps-you-prioritize-your-tasks-with-the-urgency-importance-matrix) systems.

* **Critical** means Urgent and Important.
* **High** means Urgent but not Important.
* **Medium** means Important but not Urgent.
* **Low** means Not Urgent and not Important.

The **Status** is meant to be used to indicate that someone is working on that issue, it is not possible to continue working on that issue and so on.
* **Blocked** indicates that it is not possible to resolve/process this issue yet.
* **In Process** indicates that someone is working on that issue. In addition it can be useful to assign the issue to the person working on it.

The **Type** is used to categorize the issues and should be self explanatory.

In some cases it can be useful to add further labels per category or even add additional categories such as the platform the issue belongs to.
