def serve_order(flavor):
    try:
        print(f"serving {flavor} chai...")
        if flavor=="unknown":
            raise ValueError("This flavor does not exist")
    except ValueError as e:
        print(f"Error :",e)
    else:
        print(f"chai {flavor} is served")
    finally:
        print("next customer please!")

serve_order("masala")
serve_order("unknown")