# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Mol_pro(models.Model):
    _name='mol_pro'
    _decription= 'Mo ta'
    
    p_code =fields.Char("Ma SP", requied=True)
    p_name=fields.Char('Ten SP',requied=True)
    price =fields.Float("Gia", requied=True)
    image =fields.Binary("Image")
    currency = fields.Many2one('res.currency', string='Don vi')
    desscription=fields.Char("Mo ta SP")
    
    o_item=fields.Many2many("mol_orderitem", string="Orderitem")
    
    quantity=fields.Integer("So Luong",compute='Tru_SL',inverse='Cong_SL',readonly= False,store=True)
    quantity_purchased = fields.Integer('So Luong Mua')
    
    @api.depends('quantity_purchased')
    def Tru_SL(self):
        for r in self:
            if r.quantity_purchased:
                r.quantity = r.quantity - 1
    
    def Cong_SL(self):
        for r in self:
            if r.quantity_purchased:
                r.quantity = r.quantity + 1
    def quantity_purchased_1(self):
        self.quantity_purchased = self.quantity_purchased + 1
    def quantity_purchased_2(self):
        self.quantity_purchased = self.quantity_purchased - 1
        kq=fa