# -*- coding: utf-8 -*-
# Copyright (c) 2021, SD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document



class Meeting(Document):
	def before_save(self):
		if self.to_date < self.from_date:
			frappe.throw("To date must be grater than from date")

	# def validate(self):
	# 	data = frappe.get_doc("Meeting",{"status": "Cancelled"})
	# 	for i in data:
	# 		frappe.throw("just check")

	