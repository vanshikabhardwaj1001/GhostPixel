#!/usr/bin/env python3

import os
import sys
from PIL import Image
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

# Import your existing modules
import encoder
import decoder

console = Console()


# ============================================================
# BANNER
# ============================================================

def show_banner():

    banner = r"""
   ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
  ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
  ██║  ███╗███████║██║   ██║███████╗   ██║
  ██║   ██║██╔══██║██║   ██║╚════██║   ██║
  ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║
   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝

             G H O S T P I X E L
       Image Steganography Security Tool
    """

    console.print(
        Panel(
            banner,
            border_style="cyan",
            box=box.DOUBLE,
            padding=(0, 2)
        )
    )

    console.print(
        "[bold cyan]Stealth Mode:[/bold cyan] "
        "[bold green]ON[/bold green]"
    )

    console.print(
        "[dim]Secure • Hide • Extract • Detect[/dim]\n"
    )


# ============================================================
# ENCODE
# ============================================================

def encode_secret():

    console.print(
        Panel(
            "[bold cyan]1. ENCODE SECRET MESSAGE[/bold cyan]",
            border_style="cyan"
        )
    )

    input_image = input(
        "Enter input image path: "
    ).strip()

    if not os.path.exists(input_image):

        console.print(
            "[bold red][!] File not found.[/bold red]"
        )
        return

    output_image = input(
        "Enter output image path: "
    ).strip()

    message = input(
        "Enter secret message: "
    )

    password = input(
        "Enter password: "
    )

    try:

        # Encrypt message using your crypto.py
        from crypto import encrypt_message

        encrypted_data = encrypt_message(
            message,
            password
        )

        # Send encrypted data to encoder
        encoder.encode(
            input_image,
            output_image,
            encrypted_data
        )

        console.print(
            "\n[bold green][+] Secret message encoded successfully![/bold green]"
        )

        console.print(
            f"[cyan]Output:[/cyan] {output_image}"
        )

    except Exception as e:

        console.print(
            f"[bold red][!] Encoding failed: {e}[/bold red]"
        )


# ============================================================
# DECODE
# ============================================================

def decode_secret():

    console.print(
        Panel(
            "[bold cyan]2. DECODE SECRET MESSAGE[/bold cyan]",
            border_style="cyan"
        )
    )

    image_path = input(
        "Enter stego image path: "
    ).strip()

    if not os.path.exists(image_path):

        console.print(
            "[bold red][!] File not found.[/bold red]"
        )
        return

    password = input(
        "Enter password: "
    )

    try:

        from crypto import decrypt_message

        # Extract encrypted data
        encrypted_data = decoder.decode(
            image_path
        )

        # Decrypt it
        message = decrypt_message(
            encrypted_data,
            password
        )

        console.print(
            "\n[bold green][+] Secret message recovered![/bold green]"
        )

        console.print(
            Panel(
                message,
                title="Hidden Message",
                border_style="green"
            )
        )

    except Exception:

        console.print(
            "\n[bold red][!] Unable to decode message.[/bold red]"
        )

        console.print(
            "[yellow]Check the password and image.[/yellow]"
        )


# ============================================================
# DETECT
# ============================================================

def detect_hidden_data():

    console.print(
        Panel(
            "[bold cyan]3. DETECT HIDDEN DATA[/bold cyan]",
            border_style="cyan"
        )
    )

    image_path = input(
        "Enter image path: "
    ).strip()

    if not os.path.exists(image_path):

        console.print(
            "[bold red][!] File not found.[/bold red]"
        )
        return

    try:

        data = decoder.decode(
            image_path
        )

        console.print(
            "\n[bold green][+] Hidden data detected![/bold green]"
        )

        console.print(
            f"[cyan]Extracted data size:[/cyan] "
            f"{len(data)} bytes"
        )

    except Exception:

        console.print(
            "\n[bold yellow][-] No recognizable hidden data detected.[/bold yellow]"
        )


# ============================================================
# IMAGE INFORMATION
# ============================================================

def image_information():

    console.print(
        Panel(
            "[bold cyan]4. IMAGE INFORMATION[/bold cyan]",
            border_style="cyan"
        )
    )

    image_path = input(
        "Enter image path: "
    ).strip()

    if not os.path.exists(image_path):

        console.print(
            "[bold red][!] File not found.[/bold red]"
        )
        return

    try:

        image = Image.open(image_path)

        width, height = image.size
        mode = image.mode
        format_name = image.format

        pixels = width * height

        # RGB = 3 bits per pixel for basic LSB
        if mode == "RGB":
            capacity = (pixels * 3) // 8

        elif mode == "RGBA":
            capacity = (pixels * 4) // 8

        else:
            capacity = (pixels * 3) // 8

        table = Table(
            title="IMAGE INFORMATION",
            box=box.ROUNDED
        )

        table.add_column(
            "Property",
            style="cyan"
        )

        table.add_column(
            "Value",
            style="green"
        )

        table.add_row(
            "File",
            image_path
        )

        table.add_row(
            "Format",
            str(format_name)
        )

        table.add_row(
            "Width",
            str(width)
        )

        table.add_row(
            "Height",
            str(height)
        )

        table.add_row(
            "Color Mode",
            mode
        )

        table.add_row(
            "Total Pixels",
            f"{pixels:,}"
        )

        table.add_row(
            "Approx. LSB Capacity",
            f"{capacity:,} bytes"
        )

        console.print(table)

    except Exception as e:

        console.print(
            f"[bold red][!] Error: {e}[/bold red]"
        )


# ============================================================
# HELP / ABOUT
# ============================================================

def help_about():

    console.print(
        Panel(
            """
[bold cyan]GHOSTPIXEL[/bold cyan]

Image Steganography Security Tool

[bold]Features[/bold]

[1] Encode Secret Message
    Hide a message inside an image.

[2] Decode Secret Message
    Extract a hidden message.

[3] Detect Hidden Data
    Check an image for hidden data.

[4] Image Information
    Display image properties and capacity.

[5] Help / About
    Display information about GhostPixel.

[6] Exit
    Close the application.

[bold yellow]Technology[/bold yellow]

• Python
• LSB Steganography
• PNG Images
• AES-GCM Encryption
• PBKDF2 Password Derivation

[dim]GhostPixel v1.0.0[/dim]
            """,
            title="[bold cyan]ABOUT GHOSTPIXEL[/bold cyan]",
            border_style="cyan",
            box=box.DOUBLE
        )
    )


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():

    while True:

        console.print(
            Panel(
                """
[bold cyan][1][/bold cyan]  Encode Secret Message

[bold cyan][2][/bold cyan]  Decode Secret Message

[bold cyan][3][/bold cyan]  Detect Hidden Data

[bold cyan][4][/bold cyan]  Image Information

[bold cyan][5][/bold cyan]  Help / About

[bold red][6][/bold red]  Exit
                """,
                title="[bold cyan]GHOSTPIXEL MENU[/bold cyan]",
                border_style="bright_blue",
                box=box.DOUBLE
            )
        )

        choice = input(
            "GhostPixel > "
        ).strip()

        if choice == "1":

            encode_secret()

        elif choice == "2":

            decode_secret()

        elif choice == "3":

            detect_hidden_data()

        elif choice == "4":

            image_information()

        elif choice == "5":

            help_about()

        elif choice == "6":

            console.print(
                "\n[bold cyan]GhostPixel shutting down...[/bold cyan]"
            )

            console.print(
                "[dim]Stay invisible. Stay secure. 👻[/dim]"
            )

            sys.exit(0)

        else:

            console.print(
                "[bold red][!] Invalid option.[/bold red]"
            )

        input(
            "\nPress Enter to return to menu..."
        )

        os.system("clear")

        show_banner()


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    os.system("clear")

    show_banner()

    main_menu()