# -*- coding: utf-8 -*-
# from odoo import http


# class AiMeetingAssistant(http.Controller):
#     @http.route('/ai_meeting_assistant/ai_meeting_assistant', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ai_meeting_assistant/ai_meeting_assistant/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ai_meeting_assistant.listing', {
#             'root': '/ai_meeting_assistant/ai_meeting_assistant',
#             'objects': http.request.env['ai_meeting_assistant.ai_meeting_assistant'].search([]),
#         })

#     @http.route('/ai_meeting_assistant/ai_meeting_assistant/objects/<model("ai_meeting_assistant.ai_meeting_assistant"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ai_meeting_assistant.object', {
#             'object': obj
#         })

