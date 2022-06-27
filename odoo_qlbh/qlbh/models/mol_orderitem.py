# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Mol_orderitem(models.Model):
    _name='mol_orderitem'
    _decription= 'Mo ta'
    
    
    o_code=fields.Char("Ma order", requied=True)
    name_pro=fields.Many2many('mol_pro', string="Ten SP")
    
    # quantity=fields.Float("So luong",compute='_tru_sach',readonly= False,store=True)
    # so_luong_mua = fields.Integer('so luong mua')
    #
    # @api.depends('so_luong_mua')
    # def _tru_sach(self):
    #     for r in self:
    #         if r.so_luong_mua:
    #             r.quantity = r.quantity - 1
    #
    # def so_luong_mua_1(self):
    #     self.so_luong_mua = self.so_luong_mua + 1