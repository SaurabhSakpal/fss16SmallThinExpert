"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):

	def has_two_pair(self):
		all_cards = []
		for card_list in self.suits.values():
			for card in card_list:
				all_cards.append(card)
		
		sorted_cards = sorted(all_cards)
		
		flag = 0
		
		for i in range(1, len(sorted_cards)):
			if sorted_cards[i] == sorted_cards[i-1]:
				flag += 1
				if flag == 2:
					return True
			
		return False

	def has_full_house(self):
		three_rank = -1
		two_rank = -1
		for rank in range(1,14):
			count = 0
			for suit in range(0,4):
				if suit not in self.suits:
					continue
				if rank in self.suits[suit]:
					count += 1 
				if count >= 3:
					three_rank = rank

		if three_rank == -1:
			return False

		for rank in range(1,14):
			if rank==three_rank:
				continue
			count = 0
			for suit in range(0,4):
				if suit not in self.suits:
					continue
				if rank in self.suits[suit]:
					count += 1 
				if count >= 2:
					two_rank = rank
					if three_rank != two_rank:
						return True
		return False


	def has_N_of_a_kind(self,N):
		for rank in range(1,14):
			count = 0;
			for suit in range(0,4):
				if suit not in self.suits:
					continue
				if rank in self.suits[suit]:
					count += 1 
				if count >= N:
					return True
		return False

	def has_pair(self):
		return self.has_N_of_a_kind(2)

	def has_three_of_a_kind(self):
		return self.has_N_of_a_kind(3)

	def has_four_of_a_kind(self):
		return self.has_N_of_a_kind(4)

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


	def has_straight(self) :
		""" Returns True if the hand has a straight, False otherwise 
		"""
		cumulativeList = [];
		for card_list in self.suits.values():
			if card_list != None :
				for j in range(len(card_list)) :
					cumulativeList.append(card_list[j])
		sorted_cards = sorted(cumulativeList)
		previous = -1
		unduplicated_list = []
		for i in range(len(sorted_cards)):
			if previous != sorted_cards[i] :
				unduplicated_list.append(sorted_cards[i])
				previous = sorted_cards[i]
		if self.checkIfStraight(unduplicated_list):
			return True;
		return False

def classify(hand):
	if hand.has_straight_flush():
		return "straight_flush"
	elif hand.has_four_of_a_kind():
		return "four_of_a_kind"
	elif hand.has_full_house():
		return "full_house"
	elif hand.has_flush():
		return "flush"
	elif hand.has_straight():
		return "straight"
	elif hand.has_three_of_a_kind():
		return "three_of_a_kind"
	elif hand.has_two_pair():
		return "two_pair"
	elif hand.has_pair():
		return "pair"

def printTable(prob_table,N):

	for hand in prob_table.keys():
		print hand.ljust(20).upper(), float(prob_table[hand])/N


def find_probability(N):
		
		prob_table = { "straight_flush": 0, "four_of_a_kind": 0, "full_house": 0, "flush": 0, 
		"straight": 0, "three_of_a_kind": 0, "two_pair": 0, "pair": 0 }

		for i in range(N):
			
			deck = Deck()
			deck.shuffle()
			
			hand = PokerHand()
			deck.move_cards(hand, 7)
			hand.suit_hist()	
			
			label = classify(hand)

			if label == "straight_flush" :
				prob_table["straight_flush"] += 1 
			elif label == "four_of_a_kind":
				prob_table["four_of_a_kind"] += 1
			elif label == "full_house":
				prob_table["full_house"] += 1 
			elif label == "flush":
				prob_table["flush"] += 1	
			elif label == "straight":
				prob_table["straight"] += 1
			elif label == "three_of_a_kind":
				prob_table["three_of_a_kind"] += 1
			elif label == "two_pair":
				prob_table["two_pair"] += 1
			elif label == "pair":
				prob_table["pair"] += 1
			
	
		printTable(prob_table,N)

if __name__ == '__main__':

	find_probability(10000)

