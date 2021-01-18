# -*- coding: utf-8 -*-
# Copyright (c) 2021, SD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class EnrollmentForm(WebsiteGenerator):
	def validate(self):
		doc = frappe.new_doc("User")
		doc.first_name = self.first_name
		doc.full_name = self.full_name
		doc.email = self.email
		doc.save()

	def after_insert(self):
		frappe.sendmail(recipients=[self.email], message="Thanks for registration for the"+ self.conference)


