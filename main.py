import random
from typing import List, Dict, Optional

class Lead:
    def __init__(self, lead_id, location, category, quality_score):
        self.lead_id = lead_id
        self.location = location
        self.category = category
        self.quality_score = quality_score


class Partner:
    def __init__(self, partner_id, categories, locations, base_bid, max_capacity, conversion_rate):
        self.partner_id = partner_id
        self.categories = categories
        self.locations = locations
        self.base_bid = base_bid
        self.max_capacity = max_capacity
        self.current_load = 0
        self.conversion_rate = conversion_rate

    def is_eligible(self, lead):
        return (
            lead.category in self.categories
            and lead.location in self.locations
            and self.current_load < self.max_capacity
        )

    def generate_bid(self, lead):
        return self.base_bid * (0.5 + lead.quality_score)

    def expected_value(self, bid):
        return bid * self.conversion_rate


class LeadRouter:
    def __init__(self, partners):
        self.partners = partners

    def route(self, lead):
        eligible = [p for p in self.partners if p.is_eligible(lead)]

        if not eligible:
            print("No eligible partners")
            return

        best_partner = None
        best_value = -1
        best_bid = 0

        for p in eligible:
            bid = p.generate_bid(lead)
            value = p.expected_value(bid)

            print(f"Partner {p.partner_id} bid: {bid:.2f}, value: {value:.2f}")

            if value > best_value:
                best_value = value
                best_partner = p
                best_bid = bid

        print("\nWINNER:")
        print({
            "lead_id": lead.lead_id,
            "partner_id": best_partner.partner_id,
            "bid": best_bid,
        })


# RUN TEST
partners = [
    Partner("A", ["insurance"], ["FL", "CA"], 20, 5, 0.2),
    Partner("B", ["insurance"], ["FL"], 25, 3, 0.15),
    Partner("C", ["insurance"], ["TX"], 30, 10, 0.25),
]

router = LeadRouter(partners)

lead = Lead("L123", "FL", "insurance", 0.8)

router.route(lead)