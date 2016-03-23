# This file is part of Shoop.
#
# Copyright (c) 2012-2016, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from django.db import models
from django.utils.translation import ugettext_lazy as _

from shoop.core.models import Contact, ContactGroup, Shop
from shoop.utils.analog import define_log_model


class MailchimpBaseModel(models.Model):
    shop = models.ForeignKey(Shop, related_name="+", on_delete=models.CASCADE, verbose_name=_("shop"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("updated"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    sent_to_mailchimp = models.DateTimeField(null=True, verbose_name=_("sent to mailchimp"))
    latest_push_failed = models.NullBooleanField(verbose_name=_("latest push failed"))
    mailchimp_id = models.CharField(max_length=160, null=True, verbose_name=_("mailchimp id"))

    class Meta:
        abstract = True
        unique_together = ("shop", "mailchimp_id")

class MailchimpContact(MailchimpBaseModel):
    contact = models.ForeignKey(Contact, verbose_name=_("contact"))
    # TODO: add contact email for cases it changes we can take action

    class Meta:
        abstract = False


class MailchimpContactGroup(MailchimpBaseModel):
    group = models.ForeignKey(ContactGroup, verbose_name=_("contact group"))

    class Meta:
        abstract = False


MailchimpLogEntry = define_log_model(MailchimpContact)