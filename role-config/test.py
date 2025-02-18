import yaml
import argparse
import os

def parse_and_export_env(file_path, ad_key, output_file):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    if ad_key in data:
        with open(output_file, 'w') as outfile:
            for key, value in data[ad_key].items():
                outfile.write(f"{key}={value}\n")
                print(f"Written to file: {key}={value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set env variables")
    parser.add_argument("--file_path", help="base path to the role yamls")
    parser.add_argument("--role", help="role to lookup")
    parser.add_argument("--output_file", help="Path to the output file to write environment variables")
    
    args = parser.parse_args()

    
    role_to_cfg = f"/{args.file_path}/{args.role}"

    print ( f"path to config: {role_to_cfg}")
    print ( f"outputfile: {args.output_file}")

    parse_and_export_env(role_to_cfg, args.role, args.output_file)
    