from decimal import *

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def make_receipt(order, order_items, output):
        doc = SimpleDocTemplate(output, pagesize=(225,525),
                                rightMargin=1,leftMargin=1,
                                topMargin=0,bottomMargin=0)
        Story=[]
        
        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))
        
        #company detail
        ptext = "Restaurant XXXXX"
        Story.append(Paragraph(ptext, styles["Left"]))
        Story.append(Spacer(1, 6))
        
        #order detail
        ptext = "Invoice No.: " + str(order.no)
        Story.append(Paragraph(ptext, styles["Left"]))
        Story.append(Spacer(1, 6))
        
        ptext = "Created by: " + str(order.created_by.full_name)
        Story.append(Paragraph(ptext, styles["Left"]))
        Story.append(Spacer(1, 12))
        
        line = MCLine(210)
        Story.append(line)
        Story.append(Spacer(1, 6))
        
        #line item details
        data = [['Description', 'Qty', 'Price', 'Total', 'Tax']]
        total = Decimal(0.00)
        for item in order_items:
            shortname = str(item.menu.short_name)
            while len(shortname) < 18:
                shortname = shortname + " "
            
            subtotal = Decimal(item.quantity * item.price)
            total = Decimal(total + subtotal)
            itemData = [shortname, str(item.quantity), str(item.price), subtotal, "SR"]
            data.append(itemData)
        
        t = Table(data)
        t.setStyle (TableStyle([('FONTSIZE', (0, 0), (-1, -1), 9)]))
        Story.append(t)
        
        line = MCLine(210)
        Story.append(line)
        Story.append(Spacer(1, 6))
    
        #subtotal, gst, & others
        Story.append(Spacer(1, 18))
        total = Decimal(total)
        gst_total = Decimal((total * 6) /100)
        data = [['Subtotal (Excluding GST): ', '   ', '   ','   ', total],
                ['GST Payable (6%): ', '   ', '   ', '   ', gst_total]]
        t = Table(data)
        t.setStyle (TableStyle([('FONTSIZE', (0, 0), (-1, 0), 10)]))
        Story.append(t)
        
        #calculate total
        Story.append(Spacer(1, 18))
        data = [['Total:', '   ', '   ', total + gst_total]]
        t = Table(data)
        t.setStyle (TableStyle([('FONTSIZE', (0, 0), (-1, 0), 16)]))
        Story.append(t)
        
        #done, building receipt now
        Story.append(PageBreak())
        doc.build(Story)

class MCLine(Flowable):
    """
    Line flowable --- draws a line in a flowable
    http://two.pairlist.net/pipermail/reportlab-users/2005-February/003695.html
    """
 
    #----------------------------------------------------------------------
    def __init__(self, width, height=0):
        Flowable.__init__(self)
        self.width = width
        self.height = height
 
    #----------------------------------------------------------------------
    def __repr__(self):
        return "Line(w=%s)" % self.width
 
    #----------------------------------------------------------------------
    def draw(self):
        """
        draw the line
        """
        self.canv.line(0, self.height, self.width, self.height)