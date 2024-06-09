from SimulationImageMasker.ColorImageMasker.ColorValueWriter import ColorValueWriter

if __name__ == '__main__':
    input_gsd = "/Users/ethan/feldt_dKlotsa_work/KlotsaPythonCode/pythonProject1/GSDs/clone_of_modifile.gsd"
    output_gsd = "/Users/ethan/feldt_dKlotsa_work/KlotsaPythonCode/pythonProject1/GSDs/colorvalgsd.gsd"
    colorwriter = ColorValueWriter(input_gsd, output_gsd)

    colorwriter.write(0)
