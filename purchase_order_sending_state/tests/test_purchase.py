from odoo.tests.common import TransactionCase


class TestPurchaseMassSending(TransactionCase):

    def setUp(self):
        """SetUp."""
        super(TestPurchaseMassSending, self).setUp()
        group_purchase_user = self.env.ref('purchase.group_purchase_user')
        self.user = self.env['res.users'].create({
            'name': 'Purchase User',
            'login': 'user',
            'email': 'p.u@example.com',
            'signature': '--\nPU',
            'notification_type': 'email',
            'groups_id': [(6, 0, [group_purchase_user.id])]
        })
        self.partner = self.env.ref('base.res_partner_1')

    def test_purchase_order_mass_sending(self):
        # User have access Purchase/User : Create  Draft purchase order
        self.po = self.env['purchase.order'].sudo(self.user).create({'partner_id': self.partner.id})
        self.assertTrue(self.po, 'Purchase: no purchase order created')
        # Create  mail.compose.message to send Mass mailing PO
        context = {'active_model': 'purchase.order',
                   'active_ids': [self.po.id],
                   'default_composition_mode': 'mass_mail',
                   'default_partner_to': '${object.partner_id.id or \'\'}',
                   'default_use_template': True,
                   'mark_rfq_as_sent': True,
                   'default_template_id': self.env.ref('purchase.email_template_edi_purchase_done')
                   }
        mail = self.env['mail.compose.message'].with_context(context).sudo(self.user).create({
            'body': "Test Mass mailing for one PO",
            'email_from': 'po@mycompany.com'
        })
        mail.send_mail()
        # check if po is sent to supplier.
        self.assertTrue(self.po.po_sent, 'Purchase: no purchase order send')
        # create two PO and send them
        self.po1 = self.env['purchase.order'].sudo(self.user).create({'partner_id': self.partner.id})
        self.po2 = self.env['purchase.order'].sudo(self.user).create({'partner_id': self.partner.id})
        context.update({'active_ids': [self.po1.id, self.po2.id]})
        mail = self.env['mail.compose.message'].with_context(context).sudo(self.user).create({
            'body': "Test Mass mailing for multi PO",
            'email_from': 'po@mycompany.com'
        })
        mail.send_mail()
        # Purchase order confirm
        self.assertTrue(self.po1.po_sent, 'Purchase: no P1 send')
        self.assertTrue(self.po2.po_sent, 'Purchase: no P2 send')
