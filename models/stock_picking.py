from odoo import models

class StockPicking(models.Model):
    _inherit = "stock.picking"

    def _get_barcode_view_state(self):
        res = super()._get_barcode_view_state()

        for picking in res.get("records", []):
            for line in picking.get("lines", []):
                move_id = line.get("move_id")
                if not move_id:
                    line["x_studio_posiciones"] = ""
                    continue

                move = self.env["stock.move"].browse(move_id)

                # many2many → string legible
                line["x_studio_posiciones"] = ", ".join(
                    move.x_studio_posiciones.mapped("display_name")
                ) if move.x_studio_posiciones else ""

        return res
