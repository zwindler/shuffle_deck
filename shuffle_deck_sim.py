#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt
import random

switch_to_interactive = False

def split_deck_in_two(deck, imprecision):
  global switch_to_interactive
  deck_length = len(deck)
  #print(deck_length)
  deck_cut = random.randint(deck_length/2-imprecision, deck_length/2+imprecision)
  if switch_to_interactive:
    print "Cutting deck at "+str(deck_cut)+"th card"
  return deck[0:deck_cut],deck[deck_cut:deck_length]

def shuffle_deck_once(deck, imprecision, current_iter):
  global switch_to_interactive
  new_deck = []
  deck_first_half, deck_second_half = split_deck_in_two(deck, imprecision)
  deck_first_half_length = len(deck_first_half)
  deck_second_half_length = len(deck_second_half)
  min_half_length = min(deck_first_half_length,deck_second_half_length)
  #print deck_first_half_length
  #print deck_second_half_length
  #print(deck_first_half)
  #print(deck_second_half)
  for i in range(0,min_half_length):
    new_deck.append(deck_first_half[i])
    new_deck.append(deck_second_half[i])
    #print(new_deck)
  if deck_first_half_length > min_half_length:
     remaining_cards = deck_first_half[min_half_length:deck_first_half_length+1]
     #print(remaining_cards)
     for card in remaining_cards:
       new_deck.append(card)
  elif deck_second_half_length > min_half_length:
     remaining_cards = deck_second_half[min_half_length:deck_second_half_length+1]
     #print(remaining_cards)
     for card in remaining_cards:
       new_deck.append(card)
  deck_stats(new_deck, imprecision, current_iter)
  return new_deck

def shuffle_deck(deck, imprecision, iterations):
  for i in range(1,iterations+1):
    deck = shuffle_deck_once(deck, imprecision, i)

def gen_deck(deck_size):
  global switch_to_interactive
  init_deck = []
  for i in range(1,deck_size/3+1):
    init_deck.append("L")
    init_deck.append("R")
    init_deck.append("C")
  if switch_to_interactive:
    print init_deck
  else:
    print "imprecision,current_iteration,max_dist_with_no_land,max_successive_lands"
  return init_deck

def deck_stats(deck, imprecision, current_iter):
  global switch_to_interactive
  if switch_to_interactive:
    print(deck)
  max_dist_with_no_land=0
  current_dist_with_no_land=0
  max_successive_lands=0
  current_successive_lands=0
  for card in deck:
    if card == "L":
      current_dist_with_no_land=0
      current_successive_lands += 1
    else:
      current_dist_with_no_land += 1
      current_successive_lands = 0
    if current_dist_with_no_land > max_dist_with_no_land:
      max_dist_with_no_land=current_dist_with_no_land
    if current_successive_lands > max_successive_lands:
      max_successive_lands = current_successive_lands
  if switch_to_interactive:
    print "Max distance with no land: "+str(max_dist_with_no_land)+" // Max successive lands: "+str(max_successive_lands)
  else:
    print str(imprecision)+","+str(current_iter)+","+str(max_dist_with_no_land)+","+str(max_successive_lands)

def usage():
  print "ahahahah"
  sys.exit()

def main():
  global switch_to_interactive
  imprecision=0
  iterations=5
  try:
    opts, args = getopt.getopt(sys.argv[1:], 'i:In:', ['imprecision=', 'interactive', 'iterations='])
  except getopt.GetoptError:
    usage()
    sys.exit(2)

  for o, a in opts:
    if o in ('-i', '--imprecision'):
      imprecision = int(a)
    if o in ('-I', '--interactive'):
      switch_to_interactive = True
    if o in ('-n', '--iterations'):
      iterations = int(a)

  deck = gen_deck(60)
  deck = shuffle_deck(deck,imprecision,iterations)

if __name__ == '__main__':
  main()
