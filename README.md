# The Falcon

This is a project that was inspired by ZSA's Moonlander and Voyager split keyboards. I loved how they looked and with my move to a keyboard-driven workflow, I decided that I needed to make the move. I started second-guessing myself when I saw the price, as I was a student, and I came to the realisation that I had the skills to design one.

## Features
* 36 keys per split
* Serial communication between keyboards
* USB2.0 with USB-C connectors
* Voltage protection for hot plugging
* 4 layer PCB
* RGB lighting (see the note)
* QMK compatible
* Compatible with both [Gateron Low Profile 2.0](https://www.gateron.co/products/gateron-low-profile-mechanical-switch-set) (KS-33) and [Gateron G Pro switches](https://www.gateron.co/products/gateron-switch-set)

> [!NOTE]
> I have not been able to get the RGB lighting to work. I have checked the PCB schematic and nothing stands out as the error but I could be wrong. I believe that the problem comes down to the firmware implementation and drivers.

### PCB
The PCB folder contains files for the left and right PCBs separately as well as a panelised version that combines them. The PCBs were designed by me with inspiration from other similar projects. Although four layers increase the production cost, they were intentionally kept to ensure proper signal integrity and return paths, especially due to the fast switching of multiple lines for RGB, PWM and the USB differential pair.

### Case
The SolidWorks folder contains all of the CAD files that I made for the case/switch panel. 
The folders ending with _Threaded are for the initial case designs when I had initial ideas of having the case CNCed. They have threaded pillars used for screwing the bottom plate into the top, with the top also housing the keyboard switches. 
The folders with _ScrewHoles contain a full CAD design for the case, with a bottom case being used along with M2.5 screws and hex standoffs to attach to the switch panel. The switch panel was made using FR-4 and placed alongside the PCB order. Two versions of this were made, one for 'normal' switches and an adjusted one for low-profile switches.
