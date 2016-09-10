"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):

	def suit_hist(self):
		"""Builds a histogram of the suits that appear in the hand.

		Stores the result in attribute suits.
		"""
		self.suits = {}
		for card in self.cards:
			if card.suit not in self.suits:
				self.suits[card.suit]= []
			self.suits[card.suit] += [card.rank]

	def has_flush(self):
		"""Returns True if the hand has a flush, False otherwise.
	  
		Note that this works correctly for hands with more than 5 cards.
		"""
		for card_list in self.suits.values():
			if len(card_list) >= 5:
				return True
		return False

	def has_straight_flush(self):
		"""Returns True if the hand has a straight flush, False otherwise.
		"""
		for card_list in self.suits.values:
			if len(card_list) < 5:
				continue
			count = 1
			for i in range(2,len(card_list)):
				if card_list[i] == card_list[i-1]:
					count += 1
					if count==5:
						return True
				else:
					count = 1
		return False


if __name__ == '__main__':
	# make a deck
	deck = Deck()
	deck.shuffle()

	# deal the cards and classify the hands
	for i in range(7):
		hand = PokerHand()
		deck.move_cards(hand, 7)
		hand.sort()
		hand.suit_hist()

		print hand
		print hand.has_flush()
		print ''

