import argparse
import subprocess

def generate_vpc():
    arguments = ["sample.py", "--out_dir=out-vpc-char", "--device=cpu"]#, "--num_samples=5"]
    input_file = "in/out/input.txt"
    with open(input_file, "w") as output_file:
        subprocess.run(["python"] + arguments, stdout=output_file)
    movedata = "in/out/movedata.py"
    subprocess.run(["python" , movedata])

def hello():
    print("hello")






def main():
    parser = argparse.ArgumentParser(description="Script to execute specific functions.")
    parser.add_argument("function", choices=["generate_vpc","hello"], help="Select the function to execute.")

    args = parser.parse_args()

    if args.function == "generate_vpc":
        generate_vpc()

    
    if args.function == "hello":
        hello()


if __name__ == "__main__":
    main()
