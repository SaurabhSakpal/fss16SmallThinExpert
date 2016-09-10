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
			print "adding card", card
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

	def checkIfStraight(self, sorted_cards):
		if sorted_cards[0]==1:
			sorted_cards.append(14)
		for i in range(4,len(sorted_cards)):
			if sorted_cards[i]-sorted_cards[i-4] == 4:
				return True;
		return False;

	def has_straight_flush(self):
		"""Returns True if the hand has a straight flush, False otherwise.
		"""
		for card_list in self.suits.values():
			if len(card_list) < 5:
				continue
			sorted_cards = sorted(card_list)
			if self.checkIfStraight(sorted_cards):
				return True;
		return False


	def straight(self) :
		""" Returns True if the hand has a straight, False otherwise 
		"""
		cumulativeList = [];
		for card_list in self.suits.values():
			if card_list != None :
				for j in range(len(card_list)) :
					cumulativeList.append(card_list[j])
		print cumulativeList
		sorted_cards = sorted(cumulativeList)
		previous = -1
		unduplicated_list = []
		for i in range(len(sorted_cards)):
			if previous != sorted_cards[i] :
				unduplicated_list.append(sorted_cards[i])
				previous = sorted_cards[i]
		print unduplicated_list
		if self.checkIfStraight(unduplicated_list):
			return True;
		return False



if __name__ == '__main__':
	# make a deck
	deck = Deck()
	deck.shuffle()

	# deal the cards and classify the hands
	for i in range(1):
		# hand = PokerHand()
		# deck.move_cards(hand, 7)
		# hand.sort()
		# hand.suit_hist()
		hand2 = PokerHand()
		hand2.add_card(Card(0,1))
		hand2.add_card(Card(1,1))
		hand2.add_card(Card(1,10))
		hand2.add_card(Card(1,7))
		hand2.add_card(Card(1,12))
		hand2.add_card(Card(1,13))
		hand2.add_card(Card(1,11))
		hand2.suit_hist()
		print hand2
		print hand2.has_straight_flush()
		print ''

