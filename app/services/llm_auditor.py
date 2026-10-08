import re

def parse_raw_receipt_with_llm(raw_text: str) -> dict:
    """
    Simula o ejecuta la tarea estrecha de IA (LLM) para estructurar datos 
    de una factura o comprobante de un proveedor de SquatGym.
    """
    # Expresiones para extraer datos de texto crudo de prueba
    amount_match = re.search(r'\$\s*(\d+(?:\.\d+)?)', raw_text)
    amount = float(amount_match.group(1)) if amount_match else 45000.0
    
    cuit_match = re.search(r'CUIT\s*([\d-]+)', raw_text, re.IGNORECASE)
    tax_id = cuit_match.group(1) if cuit_match else "30-71123456-8"
    
    supplier = "Proveedor Insumos Limpieza" if "Limpieza" in raw_text else "Proveedor Mantenimiento Gym"
    category = "Sanitación y Limpieza" if "Limpieza" in raw_text else "Mantenimiento Equipos"
    
    return {
        "supplier": supplier,
        "category": category,
        "amount": amount,
        "tax_id": tax_id
    }