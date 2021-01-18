// Copyright (c) 2021, SD and contributors
// For license information, please see license.txt

frappe.ui.form.on('Organizer', {
	refresh: function(frm) {
		frm.add_custom_button('Create Meeting', ()=> {
			frappe.new_doc('Meeting', {
				meeting:frm.doc.meeting
			})
		})	
		frm.add_custom_button('Create Conference', ()=> {
			frappe.new_doc('Conference', {
				conference:frm.doc.Conference
			})
		})	

	}

});
