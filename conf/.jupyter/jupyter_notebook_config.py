c = get_config()
c.IPKernelApp.pylab = 'inline'  # in-line figure when using Matplotlib
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.notebook_dir = '/notebooks'
c.NotebookApp.allow_origin = '*'
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}

# do not open a browser window by default when using notebooks
c.NotebookApp.open_browser = False

# No token. Always use jupyter over ssh tunnel
c.NotebookApp.token = ''

# Allow to run Jupyter from root user inside Docker container
c.NotebookApp.allow_root = True
