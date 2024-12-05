
# Upload folder for project files 
def project_dir(instance, filename):
    return "projects/{0}/{1}".format(instance.coordinator.user.username, filename)

# Upload folder for leave files 
def leave_dir(instance, filename):
    return "leaves/{0}/{1}".format(instance.applicant.user.username, filename)

# Upload folder for leave files 
def timesheets_dir(instance, filename):
    return "timesheets/{0}/{1}".format(instance.applicant.user.username, filename)