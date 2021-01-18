# -*- coding: utf-8 -*-
# Copyright (c) 2021, SD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import utils




class Meeting_Completed(Document):
	pass



@frappe.whitelist()
def update_event():
	data = frappe.db.get_values('Meeting', {'to_date':['<', '2021-01-11']}) #date_time_objecte
	data1 = list(data)
	out = [item for t in data1 for item in t]
	for i in out:
		doc = frappe.get_doc("Meeting", i)
		doc.status == "Completed"
		doc.save()
		# data = frappe.get_doc("Meeting_completed")
		# data.meeting = i
		# data.save()





#bench execute meetings.meetings.doctype.meeting_completed.meeting_completed.scheduler_status --this is the path