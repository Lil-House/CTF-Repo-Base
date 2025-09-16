FROM ghcr.io/gzctf/challenge-base/flask:alpine

COPY --chown=ctf:ctf --chmod=700 src/ /home/ctf/

WORKDIR /home/ctf
USER ctf

CMD ["./init.sh"]