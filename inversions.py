import sys
import unittest

inv = 0

class MegaAwesomeTest(unittest.TestCase):
  def test(self):
    global inv

    lines = [line.strip() for line in open('sampleinput.txt')]
    for line in lines:
      l = [int(n) for n in line.split()]
     # print l
      nums = calcInversion(l)
     #   print "Sorted Array: ", nums
      print "Inversion:    ", inv, '/n'
      inv = 0

def calcInversion(nums):
  global inv

  if len(nums) < 2:
    return nums

  mid = len(nums)/2
  left = nums[:mid]
  right = nums[mid:]

  left, right = calcInversion(left), calcInversion(right)
  
  return merge(left, right)

def merge(A, B):
  global inv

  result = []
  i, j = 0, 0
  while i < len(A) and j < len(B):
    if A[i] <= B[j]:
      result.append(A[i])
      i = i + 1
    else:
      result.append(B[j])
      j = j + 1
      inv = inv + (len(A)-i)
  while i < len(A):
    result.append(A[i])
    i = i + 1
  while j < len(B):
    result.append(B[j])
    j = j + 1
  return result

def main():
  global inv
  lines = [line.strip() for line in open('sampleinput.txt')]
  for line in lines:
    l = [int(n) for n in line.split()]
    print l
    nums = calcInversion(l)
    print "Inversion = ", inv
    inv = 0

if __name__ == '__main__':
  unittest.main()
