# -*- coding: utf-8 -*-
# Copyright (c) 2021, SD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class Conference(WebsiteGenerator):
	def before_save(self):
		if self.to_date < self.from_date:
			frappe.throw("To date must be later than from date!")

	# def before_submit(self):
	# 	exists = frappe.db.exists(
	# 		"Conference",{
	# 		"conference":self.conference,
	# 		"docstatus":0,
	# 		"to_date":(">", self.from_date),
	# 		},
	# 		)
	# 	if not exists:
	# 		frappe.throw("To date must be later than from date!")