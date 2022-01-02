from collections import namedtuple, defaultdict, Counter
from enum import Enum
from typing import Sequence

Suit = Enum("Suit", list("SHDC"))
Rank = Enum("Rank", list("AKQJT98765432"))
Card = namedtuple("Card", ["suit", "rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


class BridgeHand:
    def __init__(self, cards: Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        if not cards or not isinstance(cards, Sequence):
            raise TypeError()
        if not all([isinstance(card, Card) for card in cards]):
            raise ValueError()
        if len(cards) != 13:
            raise ValueError()
        self.cards = cards

    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """
        return_string = ""
        card_dict = defaultdict(list)
        for card in self.cards:
            card_dict[card.suit.name].append(card.rank.name)
        suit_order = ["S", "H", "D", "C"]
        space = 0
        for idx, suit in enumerate(suit_order):
            if suit in card_dict:
                return_string += " "*space + suit + ":"
                space = 1
                for rank in Rank._member_names_:
                    for r in card_dict[suit]:
                        if r == rank:
                            return_string += r
        return return_string

    @property
    def hcp(self) -> int:
        """ Return the number of high card points contained in this hand """
        hcps = [HCP[card.rank] for card in self.cards if card.rank in HCP]
        return sum(hcps)


    @property
    def doubletons(self) -> int:
        """ Return the number of doubletons contained in this hand """
        card_strings = str(self).split()
        ranks = [cards.split(":")[1] for cards in card_strings]
        count = sum([1 for rank in ranks if len(rank) == 2])
        return count

    @property
    def singletons(self) -> int:
        """ Return the number of singletons contained in this hand """
        card_strings = str(self).split()
        ranks = [cards.split(":")[1] for cards in card_strings]
        count = sum([1 for rank in ranks if len(rank) == 1])
        return count

    @property
    def voids(self) -> int:
        """ Return the number of voids (missing suits) contained in
            this hand
        """
        card_strings = str(self).split()
        return 4 - len(card_strings)

    @property
    def ssp(self) -> int:
        """ Return the number of short suit points in this hand.
            Doubletons are worth one point, singletons two points,
            voids 3 points
        """
        return SSP[2]*self.doubletons + SSP[1]*self.singletons + SSP[0]*self.voids

    @property
    def total_points(self) -> int:
        """ Return the total points (hcp and ssp) contained in this hand """
        return self.hcp + self.ssp

    @property
    def ltc(self) -> int:
        """ Return the losing trick count for this hand - see bite description
            for the procedure
        """
        ltc = 0
        card_strings = str(self).split()
        ranks = [cards.split(":")[1] for cards in card_strings]
        for rank in ranks:
            rank = rank[:3]
            if len(rank) == 1 and rank[0] != 'A':
                ltc += 1
            elif len(rank) == 2:
                if rank != 'AK':
                    if rank[0] == 'A' or rank[0] == 'K':
                        ltc += 1
                    else:
                        ltc += 2
            elif len(rank) == 3:
                if rank != 'AKQ':
                    if rank[:2] == 'AK' or rank[:2] == 'AQ' or rank[:2] ==  'KQ':
                        ltc += 1
                    elif rank[0] == 'A' or rank[0] == 'K' or rank[0] ==  'Q':
                        ltc += 2
                    else:
                        ltc += 3
        return ltc
