## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

# ***** On all tests collaborated with Tyler Hoff and Saul *****

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

#aspects of card we need to test
class TestCards(unittest.TestCase):

	def setUp(self):
	    self.testcard = Card(2,4)
	    self.testlarge = Card(1,12)
	    self.testdeck = Deck()
	    self.testdeck2 = Deck()
	    self.blankcard = Card()


#Card Tests
	def test_suits(self):
		self.assertEqual(self.testcard.suit,"Hearts", "Testing that the correct suit has been applied to the testcard")

	def test_cardnumber(self):
		self.assertEqual(self.testcard.rank,4)

	def test_suitnames(self):
		self.assertEqual(type(self.testcard.suit_names),type([]))

	def test_suitnamesitems(self):
		for i in self.testcard.suit_names:
			self.assertTrue(i in ["Spades","Hearts","Clubs","Diamonds"])

	def test_ranklevels(self):
		self.assertEqual(type(self.testcard.rank_levels),type([]))

	def test_ranklevelslength(self):
		self.assertEqual(len(self.testcard.rank_levels),13)

	def test_ranklevelstype(self):
		for i in self.testcard.rank_levels:
			self.assertTrue(i in range(14))

	def test_faces(self):
		self.assertEqual(type(self.testcard.faces),dict)

	def test_faces_keys(self):
		for k in self.testcard.faces:
			self.assertTrue(k in [1, 11, 12, 13])

	def test_faces_values(self):
		facescounter =0
		for k in self.testcard.faces:
			# print(self.testcard.faces[k])
			self.assertTrue(self.testcard.faces[k] in ["Ace", "Jack", "Queen", "King"])
#card instance tests
	def test_blanksuit(self):
		self.assertEqual(self.blankcard.suit, "Diamonds")

	def test_blanknumber(self):
		self.assertEqual(self.blankcard.rank, 2)

	def test_strmethod(self):
		self.assertEqual((self.blankcard.__str__()), "2 of Diamonds")

	def test_strmethodlarge(self):
		self.assertEqual((self.testlarge.__str__()), "Queen of Clubs")

#Deck Tests
	def test_deckcardsmethod(self):
		self.assertEqual(type(self.testdeck.cards),list)

	def test_decklength(self):
		self.assertEqual(len(self.testdeck.cards),52)

	def test_deckobjects(self):
		for card in self.testdeck.cards:
			self.assertEqual(type(card),Card)	

	def test_deckstrmethod(self):
		self.assertEqual(type(self.testdeck.__str__()), str)

	def test_deckstrnumber(self):
		deckstr = self.testdeck.__str__()
		splitdecklist = deckstr.split("\n")
		# print(splitdecklist[0])
		self.assertEqual(splitdecklist[0], "Ace of Diamonds", "testing that the str readouts work correctly for Deck__str__ method")

	def test_popdeck(self):
		self.testdeck.pop_card(5)
		# print (self.testdeck)
		self.assertTrue("6 of Diamonds" not in self.testdeck.__str__().split("\n"))
		self.assertEqual(51, len(self.testdeck.__str__().split("\n")))

	def test_popdeckdefault(self):
		for i in range(50):
			self.testdeck.pop_card()
		self.assertTrue("13 of Spades" not in self.testdeck.__str__().split("\n"))
		self.assertTrue("3 of Diamonds" not in self.testdeck.__str__().split("\n"))
		self.assertEqual(2, len(self.testdeck.__str__().split("\n")))

	def test_shufflemethod(self):
		testdeckstrlist = self.testdeck.__str__().split("\n")
		testpositioncardy = testdeckstrlist[40]
		testpositioncardx = testdeckstrlist[18]
		self.testdeck.shuffle()
		testdeckstrlist2 = self.testdeck.__str__().split("\n")
		testpositioncardy2 = testdeckstrlist2[40]
		testpositioncardx2 = testdeckstrlist2[18]
		doubleshuffletest = False
		if testpositioncardy2 != testpositioncardy or testpositioncardx != testpositioncardx:
			doubleshuffletest = True
		self.assertEqual(doubleshuffletest,True)
		
	def test_replacecardmethodaddextra(self):
		self.testdeck.replace_card(self.testcard)
		self.assertEqual(self.testdeck.__str__(), self.testdeck2.__str__())

	def test_sortmethodfull(self):
		self.testdeck.shuffle()
		self.testdeck.sort_cards()
		self.assertEqual(len(self.testdeck.cards),52)
		deckcount = 0
		for i in self.testdeck.cards:
			if deckcount<13:
				self.assertEqual(i.suit,"Diamonds")
			elif deckcount<26:
				self.assertEqual(i.suit,"Clubs")
			elif deckcount<39:
				self.assertEqual(i.suit,"Hearts")
			else:
				self.assertEqual(i.suit,"Spades")
			deckcount+=1

	def test_sortmethodlength(self):
		self.testdeck.shuffle()
		self.testdeck.pop_card()
		self.testdeck.sort_cards()
		self.assertEqual(len(self.testdeck.cards),51, "Testing the length of the sorted deck is consistent with amount of cards popped")

	def test_sortmethodnotfull(self):
		self.testdeck.shuffle()
		self.testdeck.pop_card()
		self.testdeck.sort_cards()
		deckcount = 0
		for i in self.testdeck.cards:
			if deckcount<12:
				self.assertEqual(i.suit,"Diamonds", "Testing the length of the sorted deck is consistent with sorted deck missing popped card")
			elif deckcount<25:
				self.assertEqual(i.suit,"Clubs", "Testing the length of the sorted deck is consistent with sorted deck missing popped card")
			elif deckcount<38:
				self.assertEqual(i.suit,"Hearts", "Testing the length of the sorted deck is consistent with sorted deck missing popped card")
			else:
				self.assertEqual(i.suit,"Spades", "Testing the length of the sorted deck is consistent with sorted deck missing popped card")
			deckcount+=1
	def test_dealhandmethodhandsize(self):
		self.assertEqual(len(self.testdeck.deal_hand(5)),5)

	def test_dealhandmethodmultiple_deckremaining(self):
		try:
			self.testdeck.deal_hand(52)
			call = True
		except:
			call = False
		self.assertEqual(call,True, "Checking if dealing a 52 card hand works")

	def test_dealhandmethodpullmorethanindeck(self):
		try:
			self.testdeck.deal_hand(53)
			call = True
		except:
			call = False
		self.assertEqual(call,False)

#Play War Game Tests

class TestWarGame(unittest.TestCase):

	def test_wargamefunction(self):
		self.assertEqual(type(play_war_game(testing=True)),tuple)
		self.assertEqual(len(play_war_game(testing=True)),3)
		self.assertEqual(type(play_war_game(testing=True)[0]),str)
		self.assertTrue(play_war_game(testing=True)[0] in ["Player1", "Player2", "Tie"])
		self.assertTrue(play_war_game(testing=True)[1] in range(52))
		self.assertTrue(play_war_game(testing=True)[2] in range(52))
		wartest = play_war_game(testing=True)
		if wartest[0] == "Player1":
			self.assertTrue(wartest[1]>wartest[2])
		elif wartest[0] == "Player2":
			self.assertTrue(wartest[1]<wartest[2])
		else:
			self.assertTrue(wartest[1]==wartest[2])

class TestShowSong(unittest.TestCase):

	def test_showsongname(self):
		print (type(show_song()))
		self.assertTrue("Winner" in show_song().__str__().split())
		


unittest.main(verbosity=2)
###########