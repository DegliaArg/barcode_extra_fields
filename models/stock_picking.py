from odoo import models

class StockPicking(models.Model):
    _inherit = "stock.picking"

    def _get_barcode_view_state(self):
        res = super()._get_barcode_view_state()

        for picking in res.get("records", []):
            for line in picking.get("lines", []):
                move_line_id = line.get("id")
                if not move_line_id:
                    continue

                move_line = self.env["stock.move.line"].browse(move_line_id)
                line["x_studio_posiciones"] = move_line.x_studio_posiciones or ""

        return res
