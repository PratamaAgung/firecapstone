from send_email import extract_contacts, extract_summary, create_template, compose_email, create_plot
import fire

def debug(name,
  template_file='templates/body.txt', \
  data_file='data_input/data.csv'):

    # // CHALLENGE 2
    # // Extract data and prepare template email
    data_dict = extract_summary(data_file)
    template = create_template(template_file)

    # Print for debugging purposes
    print(compose_email(template, name, data_dict))

    # Try to create plot 
    create_plot(data_file)


if __name__ == '__main__':
  # Export to Fire
  fire.Fire(debug)