from .mail_submission import MailSubmission


class QuickHeal(MailSubmission):
    name = "QuickHeal"
    description = "Submit the file to Quick Heal for inclusion in detections."

    mail_submission = "viruslab@quickheal.com"
    mail_subject = "Sample submitted for analysis - Reply needed"
