#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
<<<<<<< HEAD
        self.assertEqual(0, len(empty_list))
=======
        self.assertEqual(__, len(empty_list))
>>>>>>> fbdff9808b65e839ca1ae3ac1fddfbf1a368b727

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
<<<<<<< HEAD
        self.assertListEqual([1, 2], nums)

        nums.append(333)
        self.assertListEqual([1, 2, 333], nums)
=======
        self.assertListEqual([1, __], nums)

        nums.append(333)
        self.assertListEqual([1, 2, __], nums)
>>>>>>> fbdff9808b65e839ca1ae3ac1fddfbf1a368b727

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

<<<<<<< HEAD
        self.assertEqual('peanut', noms[0])
        self.assertEqual('jelly', noms[3])
        self.assertEqual('jelly', noms[-1])
        self.assertEqual('butter', noms[-3])
=======
        self.assertEqual(__, noms[0])
        self.assertEqual(__, noms[3])
        self.assertEqual(__, noms[-1])
        self.assertEqual(__, noms[-3])
>>>>>>> fbdff9808b65e839ca1ae3ac1fddfbf1a368b727

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

<<<<<<< HEAD
        self.assertEqual(['peanut'], noms[0:1])
        self.assertEqual(['peanut', 'butter'], noms[0:2])
        self.assertEqual([], noms[2:2])
        self.assertEqual(['and', 'jelly'], noms[2:20])
        self.assertEqual([], noms[4:0])
        self.assertEqual([], noms[4:100])
        self.assertEqual([], noms[5:0])
=======
        self.assertEqual(__, noms[0:1])
        self.assertEqual(__, noms[0:2])
        self.assertEqual(__, noms[2:2])
        self.assertEqual(__, noms[2:20])
        self.assertEqual(__, noms[4:0])
        self.assertEqual(__, noms[4:100])
        self.assertEqual(__, noms[5:0])
>>>>>>> fbdff9808b65e839ca1ae3ac1fddfbf1a368b727

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

<<<<<<< HEAD
        self.assertEqual(['and', 'jelly'], noms[2:])
        self.assertEqual(['peanut', 'butter'], noms[:2])
=======
        self.assertEqual(__, noms[2:])
        self.assertEqual(__, noms[:2])
>>>>>>> fbdff9808b65e839ca1ae3ac1fddfbf1a368b727

    def test_lists_and_ranges(self):
        self.assertEqual(range, type(range(5)))
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
<<<<<<< HEAD
        self.assertEqual([0,1,2,3,4], list(range(5)))
        self.assertEqual([5,6,7,8], list(range(5, 9)))

    def test_ranges_with_steps(self):
        self.assertEqual([5,4], list(range(5, 3, -1)))
        self.assertEqual([0,2,4,6], list(range(0, 8, 2)))
        self.assertEqual([1,4,7], list(range(1, 8, 3)))
        self.assertEqual([5,1,-3], list(range(5, -7, -4)))
        self.assertEqual([5,1,-3,-7], list(range(5, -8, -4)))
=======
        self.assertEqual(__, list(range(5)))
        self.assertEqual(__, list(range(5, 9)))

    def test_ranges_with_steps(self):
        self.assertEqual(__, list(range(5, 3, -1)))
        self.assertEqual(__, list(range(0, 8, 2)))
        self.assertEqual(__, list(range(1, 8, 3)))
        self.assertEqual(__, list(range(5, -7, -4)))
        self.assertEqual(__, list(range(5, -8, -4)))
>>>>>>> fbdff9808b65e839ca1ae3ac1fddfbf1a368b727

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
<<<<<<< HEAD
        self.assertEqual(['you', 'shall', 'not', 'pass'], knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(['Arthur', 'you', 'shall', 'not', 'pass'], knight)
=======
        self.assertEqual(__, knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(__, knight)
>>>>>>> fbdff9808b65e839ca1ae3ac1fddfbf1a368b727

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

<<<<<<< HEAD
        self.assertEqual([10, 20, 30, 40, 'last'], stack)

        popped_value = stack.pop()
        self.assertEqual('last', popped_value)
        self.assertEqual([10, 20, 30, 40], stack)

        popped_value = stack.pop(1)
        self.assertEqual(20, popped_value)
        self.assertEqual([10, 30, 40], stack)
=======
        self.assertEqual(__, stack)

        popped_value = stack.pop()
        self.assertEqual(__, popped_value)
        self.assertEqual(__, stack)

        popped_value = stack.pop(1)
        self.assertEqual(__, popped_value)
        self.assertEqual(__, stack)
>>>>>>> fbdff9808b65e839ca1ae3ac1fddfbf1a368b727

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

<<<<<<< HEAD
        self.assertEqual([1,2,'last'], queue)

        popped_value = queue.pop(0)
        self.assertEqual(1, popped_value)
        self.assertEqual([2,'last'], queue)
=======
        self.assertEqual(__, queue)

        popped_value = queue.pop(0)
        self.assertEqual(__, popped_value)
        self.assertEqual(__, queue)
>>>>>>> fbdff9808b65e839ca1ae3ac1fddfbf1a368b727

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

