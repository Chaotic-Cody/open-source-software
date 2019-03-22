# Lab 8

## Checkpoint 1

![p1](images/cmake_gui.png)

## Checkpoint 2

Viewing tests:
![view_tests](images/view_tests.png)


Error Submission:

Log shows the file, line number, arguments, and current directory of the error.

Error condition: SIGSEGV & SIGILL
![failed_test](images/failed_test.png)

Nightly System:

The linux-shared build is passing all tests, with only 6 warnings.

ctest -D Experimental
![local_test](images/local_test.png)

There are no errors, all 81 tests pass with my submission.

## Checkpoint 3

TestNewArrayInterpolationDense.cxx failure

![test_failure](images/test_failure.png)
![dash](images/test_failure_dash.png)

Dashboard says "Error: expected 2"

## Checkpoint 4

Debug log:

Changed 'c->SetValue(5, 1, 9);' to 'c->SetValue(4, 1, 9);'

Changed 'test_new_expression(d->GetValue(0, 1) == 4, "Error: expected 2");' to 'test_new_expression(d->GetValue(0, 1) == 2, "Error: expected 2");'

![fixed](images/fixed_test.png)

## Checkpoint 5
![p](images/project.png)