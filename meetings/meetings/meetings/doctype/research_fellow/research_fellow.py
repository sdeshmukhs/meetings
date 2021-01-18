# -*- coding: utf-8 -*-
# Copyright (c) 2021, SD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ResearchFellow(Document):
	def before_submit(self):
		if self.paid == "No":
			frappe.throw("Payment is incomplete")
