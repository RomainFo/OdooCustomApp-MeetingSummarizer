# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ai_meeting_assistant(models.Model):
    _name = 'ai_meeting_assistant.ai_meeting_assistant'
    _description = 'ai_meeting_assistant.ai_meeting_assistant'

    name = fields.Char(string="Meeting Title", required=True)
    audio_file = fields.Binary(string="Audio File", required=True)
    audio_filename = fields.Char(string="Audio Filename")
    transcript = fields.Text(string="Transcript")
    summary = fields.Text(string="Summary")
    action_points = fields.Text(string="Action Points")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("processing", "Processing"),
            ("processed", "Processed"),
            ("error", "Error"),
        ],
        default="draft",
        string="Status",
        readonly=True,
    )
    recording_date = fields.Date(string="Recording Date",default=fields.Date.today)
    complementary_info = fields.Text(string="Complementary Information")
    error_message = fields.Text(string="Error Message", readonly=True)

    def action_process_meeting(self):
        # Placeholder for processing logic
        for record in self:
            try:
                print(f"Processing meeting: {record.name}")
                #if correctly processed:
                record.transcript = "Test transcript"
                record.summary = "Test summary"
                record.action_points = "Test action point"
                record.state = "processed"

                #if error during processing:
                #record.state = "error"
            except Exception as e:
                record.state = "error"
                record.error_message = str(e)